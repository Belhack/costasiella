import gql from "graphql-tag"

export const GET_FINANCE_INVOICE_ITEM_QUERY = gql`
query financeInvoiceItem($before: String, $after: String, $accountSubscription: ID!) {
  financeInvoiceItems(before: $before, after: $after, accountSubscription:$accountSubscription) {
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
    edges {
      node {
        id
        financeInvoice {
          id
          invoiceNumber
          status
          summary
          dateSent
          dateDue
          total
          balance
        }
        subscriptionYear
        subscriptionMonth
      }
    }
  }
}

`

// export const GET_ACCOUNT_SUBSCRIPTION_CREDIT_QUERY = gql`
// query AccountSubscriptionCredit($id: ID!) {
//   accountSubscriptionCredit(id:$id) {
//     id
//     accountSubscription {
//       id
//     }
//     mutationType
//     mutationAmount
//     description
//     createdAt
//   }
// }
// `


// export const DELETE_ACCOUNT_SUBSCRIPTION_CREDIT = gql`
//   mutation DeleteAccountSubscriptionCredit($input: DeleteAccountSubscriptionCreditInput!) {
//     deleteAccountSubscriptionCredit(input: $input) {
//       ok
//     }
//   }
// `
