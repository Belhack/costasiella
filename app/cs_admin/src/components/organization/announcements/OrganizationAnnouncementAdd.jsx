// @flow

import React from 'react'
import { useMutation } from "react-apollo";
import { withTranslation } from 'react-i18next'
import { withRouter } from "react-router"
import { Formik } from 'formik'
import { toast } from 'react-toastify'
import { Link } from 'react-router-dom'

import { GET_ANNOUNCEMENTS_QUERY, ADD_ANNOUNCEMENT } from './queries'
// import { LEVEL_SCHEMA } from './yupSchema'
import OrganizationAnnouncementForm from './OrganizationAnnouncementForm'


import {
  Page,
  Grid,
  Icon,
  Button,
  Card,
  Container,
  Form,
} from "tabler-react"
import SiteWrapper from "../../SiteWrapper"
import HasPermissionWrapper from "../../HasPermissionWrapper"

import OrganizationMenu from '../OrganizationMenu'

function OrganizationAnnouncementAdd({t, history}) {
  const returnUrl = "/organization/announcements"
  const [addAnnouncement] = useMutation(ADD_ANNOUNCEMENT)
  
  return (
    <SiteWrapper>
      <div className="my-3 my-md-5">
        <Container>
          <Page.Header title={t('organization.title')} />
          <Grid.Row>
            <Grid.Col md={9}>
            <Card>
              <Card.Header>
                <Card.Title>{t('organization.levels.title_add')}</Card.Title>
              </Card.Header>
                <Formik
                    initialValues={{ 
                      displayPublic: false,
                      displayShop: false,
                      displayBackend: false,
                      title: '', 
                      content: '',
                      dateStart: new Date(),
                      dateEnd: undefined,
                      priority: 100,
                    }}
                    // validationSchema={LEVEL_SCHEMA}
                    onSubmit={(values, { setSubmitting }) => {
                        addAnnouncement({ variables: {
                          input: {
                            title: values.title, 
                          }
                        }, refetchQueries: [
                            {query: GET_ANNOUNCEMENTS_QUERY}
                        ]})
                        .then(({ data }) => {
                            console.log('got data', data);
                            toast.success((t('organization.announcements.toast_add_success')), {
                                position: toast.POSITION.BOTTOM_RIGHT
                              })
                          }).catch((error) => {
                            toast.error((t('general.toast_server_error')) + ': ' +  error, {
                                position: toast.POSITION.BOTTOM_RIGHT
                              })
                            console.log('there was an error sending the query', error)
                            setSubmitting(false)
                          })
                    }}
                    >
                    {({ isSubmitting, errors, values, setFieldTouched, setFieldValue }) => (
                        <OrganizationAnnouncementForm 
                          isSubmitting={isSubmitting}
                          values={values}
                          errors={errors}
                          setFieldTouched={setFieldTouched}
                          setFieldValue={setFieldValue}
                          returnUrl={returnUrl}
                        />
                    )}
                </Formik>
            </Card>
            </Grid.Col>
            <Grid.Col md={3}>
              <HasPermissionWrapper permission="add"
                                    resource="organizationannouncement">
                <Link to={returnUrl}>
                  <Button color="primary btn-block mb-6">
                    <Icon prefix="fe" name="chevrons-left" /> {t('general.back')}
                  </Button>
                </Link>
              </HasPermissionWrapper>
              <OrganizationMenu active_link='announcements'/>
            </Grid.Col>
          </Grid.Row>
        </Container>
      </div>
    </SiteWrapper>
  )
}


export default withTranslation()(withRouter(OrganizationAnnouncementAdd))