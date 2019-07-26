import gql from "graphql-tag"

export const GET_INVOICES_QUERY = gql`
  query FinanceInvoices {
    financeInvoices {
      pageInfo {
        hasNextPage
        hasPreviousPage
        startCursor
        endCursor
      }
      edges {
        node {
          id
          accounts {
            edges {
              node {
                id
                fullName
              }
            }
          }
          invoiceNumber
          status
          summary
          relationCompany
          relationContactName
          dateSent
          dateDue
          total
          totalDisplay
          balance
          balanceDisplay
        }
      }
    }
  }
`

export const GET_COSTCENTER_QUERY = gql`
  query FinanceCostcenter($id: ID!) {
    financeCostcenter(id:$id) {
      id
      name
      code
      archived
    }
  }
`