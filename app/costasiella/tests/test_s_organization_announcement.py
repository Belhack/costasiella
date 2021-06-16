# from graphql.error.located_error import GraphQLLocatedError
import graphql

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from graphene.test import Client
from graphql_relay import to_global_id

# Create your tests here.
from django.contrib.auth.models import AnonymousUser

from . import factories as f
from .helpers import execute_test_client_api_query
from .. import models


class GQLOrganizationAnnouncement(TestCase):
    # https://docs.djangoproject.com/en/2.1/topics/testing/overview/
    def setUp(self):
        # This is run before every test
        self.admin_user = f.AdminUserFactory.create()
        self.anon_user = AnonymousUser()

        self.permission_view = 'view_organizationannouncement'
        self.permission_add = 'add_organizationannouncement'
        self.permission_change = 'change_organizationannouncement'
        self.permission_delete = 'delete_organizationannouncement'

        self.variables_create = {
            "input": {
                "name": "New announcement",
            }
        }
        
        self.variables_update = {
            "input": {
                "name": "Updated announcement",
            }
        }

        self.variables_archive = {
            "input": {
                "archived": True
            }
        }

        self.announcements_query = '''
  query OrganizationAnnouncements($after: String, $before: String) {
    organizationAnnouncements(first: 15, before: $before, after: $after) {
      pageInfo {
        startCursor
        endCursor
        hasNextPage
        hasPreviousPage
      }
      edges {
        node {
          id
          displayPublic
          displayShop
          displayBackend
          title
          content
          dateStart
          dateEnd
          priority
        }
      }
    }
  }
'''

        self.announcement_query = '''
  query OrganizationAnnouncement($id: ID!) {
    organizationAnnouncement(id:$id) {
      id
      displayPublic
      displayShop
      displayBackend
      title
      content
      dateStart
      dateEnd
      priority
    }
  }
'''

        self.announcement_create_mutation = '''
  mutation CreateOrganizationAnnouncement($input:CreateOrganizationAnnouncementInput!) {
    createOrganizationAnnouncement(input: $input) {
      organizationAnnouncement {
        id
      }
    }
  }
'''

        self.announcement_update_mutation = '''
  mutation UpdateOrganizationAnnouncement($input: UpdateOrganizationAnnouncementInput!) {
    updateOrganizationAnnouncement(input: $input) {
      organizationAnnouncement {
        id
      }
    }
  }
'''

        self.announcement_delete_mutation = '''
mutation DeleteOrganizationAnnouncement($input: DeleteOrganizationAnnouncementInput!) {
  deleteOrganizationAnnouncement(input: $input) {
    ok
  }
}
'''

    def tearDown(self):
        # This is run after every test
        pass

    def test_query(self):
        """ Query list of announcements """
        query = self.announcements_query
        announcement = f.OrganizationAnnouncementFactory.create()

        executed = execute_test_client_api_query(query, self.admin_user)
        data = executed.get('data')
        item = data['organizationAnnouncements']['edges'][0]['node']
        self.assertEqual(item['displayPublic'], announcement.display_public)
        self.assertEqual(item['displayShop'], announcement.display_shop)
        self.assertEqual(item['displayBackend'], announcement.display_backend)
        self.assertEqual(item['title'], announcement.title)
        self.assertEqual(item['content'], announcement.content)
        self.assertEqual(item['dateStart'], str(announcement.date_start))
        self.assertEqual(item['dateEnd'], str(announcement.date_end))
        self.assertEqual(item['priority'], announcement.priority)

    def test_query_permission_denied(self):
        """ Query list of announcements as user without permissions (display_public False shouldn't be listed) """
        query = self.announcements_query
        announcement = f.OrganizationAnnouncementFactory.create()
        announcement.display_public = False
        announcement.save()

        # Create regular user
        user = f.RegularUserFactory.create()
        executed = execute_test_client_api_query(query, user)
        data = executed.get('data')

        self.assertEqual(len(data['organizationAnnouncements']['edges']), 0)

    def test_query_permission_granted(self):
        """ Query list of announcements with view permission """
        query = self.announcements_query
        non_public_announcement = f.OrganizationAnnouncementFactory.build()
        non_public_announcement.display_public = False
        non_public_announcement.save()

        # Create regular user
        user = f.RegularUserFactory.create()
        permission = Permission.objects.get(codename=self.permission_view)
        user.user_permissions.add(permission)
        user.save()

        executed = execute_test_client_api_query(query, user)
        data = executed.get('data')
        item = data['organizationAnnouncements']['edges'][0]['node']
        self.assertEqual(item['title'], non_public_announcement.title)

    def test_query_anon_user(self):
        """ Query list of announcements as anon user - archived shouldn't be visible"""
        query = self.announcements_query
        announcement = f.OrganizationAnnouncementFactory.create()
        announcement.display_public = False
        announcement.save()

        executed = execute_test_client_api_query(query, self.anon_user)
        data = executed.get('data')
        self.assertEqual(len(data['organizationAnnouncements']['edges']), 0)

    # def test_query_one(self):
    #     """ Query one announcement """
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #
    #     # First query announcements to get node id easily
    #     node_id = self.get_node_id_of_first_announcement()
    #
    #     # Now query single announcement and check
    #     query = self.announcement_query
    #     executed = execute_test_client_api_query(query, self.admin_user, variables={"id": node_id})
    #     data = executed.get('data')
    #     self.assertEqual(data['organizationAnnouncement']['name'], announcement.name)
    #     self.assertEqual(data['organizationAnnouncement']['archived'], announcement.archived)
    #
    # def test_query_one_anon_user(self):
    #     """ Deny permission to view archived announcements for anon users Query one announcement """
    #     query = self.announcement_query
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     announcement.archived = True
    #     announcement.save()
    #     node_id = to_global_id("OrganizationAnnouncementNode", announcement.id)
    #     executed = execute_test_client_api_query(query, self.anon_user, variables={"id": node_id})
    #     data = executed.get('data')
    #     self.assertEqual(data['organizationAnnouncement'], None)
    #
    # def test_query_one_archived_without_permission(self):
    #     """ None returned when user lacks authorization to view archived announcements """
    #     query = self.announcement_query
    #
    #     user = f.RegularUserFactory.create()
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     announcement.archived = True
    #     announcement.save()
    #     node_id = to_global_id("OrganizationAnnouncementNode", announcement.id)
    #
    #     executed = execute_test_client_api_query(query, user, variables={"id": node_id})
    #     data = executed.get('data')
    #     self.assertEqual(data['organizationAnnouncement'], None)
    #
    # def test_query_one_permission_granted(self):
    #     """ Respond with data when user has permission """
    #     query = self.announcement_query
    #     # Create regular user
    #     user = f.RegularUserFactory.create()
    #     permission = Permission.objects.get(codename='view_organizationannouncement')
    #     user.user_permissions.add(permission)
    #     user.save()
    #
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     node_id = self.get_node_id_of_first_announcement()
    #
    #     executed = execute_test_client_api_query(query, user, variables={"id": node_id})
    #     data = executed.get('data')
    #     self.assertEqual(data['organizationAnnouncement']['name'], announcement.name)
    #
    # def test_create_announcement(self):
    #     """ Create a announcement """
    #     query = self.announcement_create_mutation
    #     variables = self.variables_create
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         self.admin_user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     self.assertEqual(data['createOrganizationAnnouncement']['organizationAnnouncement']['name'], variables['input']['name'])
    #     self.assertEqual(data['createOrganizationAnnouncement']['organizationAnnouncement']['archived'], False)
    #
    #
    # def test_create_announcement_anon_user(self):
    #     """ Create a announcement with anonymous user, check error message """
    #     query = self.announcement_create_mutation
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         self.anon_user,
    #         variables=self.variables_create
    #     )
    #     data = executed.get('data')
    #     errors = executed.get('errors')
    #     self.assertEqual(errors[0]['message'], 'Not logged in!')
    #
    #
    # def test_create_announcement_permission_granted(self):
    #     """ Create a announcement with a user having the add permission """
    #     query = self.announcement_create_mutation
    #     variables = self.variables_create
    #
    #     # Create regular user
    #     user = f.RegularUserFactory.create()
    #     permission = Permission.objects.get(codename=self.permission_add)
    #     user.user_permissions.add(permission)
    #     user.save()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     self.assertEqual(data['createOrganizationAnnouncement']['organizationAnnouncement']['name'], variables['input']['name'])
    #     self.assertEqual(data['createOrganizationAnnouncement']['organizationAnnouncement']['archived'], False)
    #
    #
    # def test_create_announcement_permission_denied(self):
    #     """ Create a announcement with a user not having the add permission """
    #     query = self.announcement_create_mutation
    #
    #     # Create regular user
    #     user = f.RegularUserFactory.create()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         user,
    #         variables=self.variables_create
    #     )
    #     errors = executed.get('errors')
    #     self.assertEqual(errors[0]['message'], 'Permission denied!')
    #
    #
    # def test_update_announcement(self):
    #     """ Update a announcement as admin user """
    #     query = self.announcement_update_mutation
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     variables = self.variables_update
    #     variables['input']['id'] = self.get_node_id_of_first_announcement()
    #
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         self.admin_user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     self.assertEqual(data['updateOrganizationAnnouncement']['organizationAnnouncement']['name'], variables['input']['name'])
    #     self.assertEqual(data['updateOrganizationAnnouncement']['organizationAnnouncement']['archived'], False)
    #
    #
    # def test_update_announcement_anon_user(self):
    #     """ Update a announcement as anonymous user """
    #     query = self.announcement_update_mutation
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     variables = self.variables_update
    #     variables['input']['id'] = self.get_node_id_of_first_announcement()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         self.anon_user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     errors = executed.get('errors')
    #     self.assertEqual(errors[0]['message'], 'Not logged in!')
    #
    #
    # def test_update_announcement_permission_granted(self):
    #     """ Update a announcement as user with permission """
    #     query = self.announcement_update_mutation
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     variables = self.variables_update
    #     variables['input']['id'] = self.get_node_id_of_first_announcement()
    #
    #     user = f.RegularUserFactory.create()
    #     permission = Permission.objects.get(codename=self.permission_change)
    #     user.user_permissions.add(permission)
    #     user.save()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     self.assertEqual(data['updateOrganizationAnnouncement']['organizationAnnouncement']['name'], variables['input']['name'])
    #     self.assertEqual(data['updateOrganizationAnnouncement']['organizationAnnouncement']['archived'], False)
    #
    #
    # def test_update_announcement_permission_denied(self):
    #     """ Update a announcement as user without permissions """
    #     query = self.announcement_update_mutation
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     variables = self.variables_update
    #     variables['input']['id'] = self.get_node_id_of_first_announcement()
    #
    #     user = f.RegularUserFactory.create()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     errors = executed.get('errors')
    #     self.assertEqual(errors[0]['message'], 'Permission denied!')
    #
    #
    # def test_archive_announcement(self):
    #     """ Archive a announcement """
    #     query = self.announcement_delete_mutation
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     variables = self.variables_archive
    #     variables['input']['id'] = self.get_node_id_of_first_announcement()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         self.admin_user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     self.assertEqual(data['archiveOrganizationAnnouncement']['organizationAnnouncement']['archived'], variables['input']['archived'])
    #
    #
    # def test_archive_announcement_anon_user(self):
    #     """ Archive a announcement """
    #     query = self.announcement_delete_mutation
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     variables = self.variables_archive
    #     variables['input']['id'] = self.get_node_id_of_first_announcement()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         self.anon_user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     errors = executed.get('errors')
    #     self.assertEqual(errors[0]['message'], 'Not logged in!')
    #
    #
    # def test_archive_announcement_permission_granted(self):
    #     """ Allow archiving announcements for users with permissions """
    #     query = self.announcement_delete_mutation
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     variables = self.variables_archive
    #     variables['input']['id'] = self.get_node_id_of_first_announcement()
    #
    #     # Create regular user
    #     user = f.RegularUserFactory.create()
    #     permission = Permission.objects.get(codename=self.permission_delete)
    #     user.user_permissions.add(permission)
    #     user.save()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     self.assertEqual(data['archiveOrganizationAnnouncement']['organizationAnnouncement']['archived'], variables['input']['archived'])
    #
    #
    # def test_archive_announcement_permission_denied(self):
    #     """ Check archive announcement permission denied error message """
    #     query = self.announcement_delete_mutation
    #     announcement = f.OrganizationAnnouncementFactory.create()
    #     variables = self.variables_archive
    #     variables['input']['id'] = self.get_node_id_of_first_announcement()
    #
    #     # Create regular user
    #     user = f.RegularUserFactory.create()
    #
    #     executed = execute_test_client_api_query(
    #         query,
    #         user,
    #         variables=variables
    #     )
    #     data = executed.get('data')
    #     errors = executed.get('errors')
    #     self.assertEqual(errors[0]['message'], 'Permission denied!')
    #
    #
