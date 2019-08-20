import gql from "graphql-tag"


export const GET_BOOKING_OPTIONS_QUERY = gql`
  query ScheduleClassBookingOptions($account: ID!, $scheduleItem:ID!, $date:Date!, $listType:String!) {
    scheduleClassBookingOptions(account: $account, scheduleItem: $scheduleItem, date:$date, listType:$listType) {
      date
      account {
        id
        fullName
      }
      scheduleItem {
        frequencyType
        frequencyInterval
        organizationLocationRoom {
          id
          name
          organizationLocation {
            id
            name
          }
        }
        organizationClasstype {
          id
          name
        }
        organizationLevel {
          id
          name
        }
        dateStart
        dateEnd
        timeStart
        timeEnd
      }
      classpasses {
        bookingType 
        allowed
        accountClasspass {
          id
          dateStart
          dateEnd
          organizationClasspass {
            id
            name
          }
        }
      }
      subscriptions {
        bookingType
        allowed
        accountSubscription {
          id
          dateStart
          dateEnd
          organizationSubscription {
            id
            name
          }
        }
      }
    }
  }
`


// export const CHECKIN_MUTATION = gql`

// `