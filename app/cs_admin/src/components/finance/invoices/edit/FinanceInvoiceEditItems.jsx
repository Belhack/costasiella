// @flow

import React, { useCallback } from 'react'
import gql from "graphql-tag"
import { useMutation } from "react-apollo"
import { withTranslation } from 'react-i18next'
import { withRouter } from "react-router"
import { DragDropContext, Draggable, Droppable } from 'react-beautiful-dnd';
import { toast } from 'react-toastify'

import {
  Card, 
  Table
} from "tabler-react"

import UpdateProductName from "./UpdateProductName"
import UpdateDescription from "./UpdateDescription"
import UpdateQuantity from "./UpdateQuantity"
import UpdatePrice from "./UpdatePrice"
import UpdateFinanceTaxRate from "./UpdateFinanceTaxRate"
import FinanceInvoiceItemDelete from "./FinanceInvoiceItemDelete"
import FinanceInvoiceItemAdd from "./FinanceInvoiceItemAdd"
import { GET_INVOICE_QUERY } from '../queries'


export const UPDATE_INVOICE_ITEM = gql`
  mutation UpdateFinanceInvoiceItem($input: UpdateFinanceInvoiceItemInput!) {
    updateFinanceInvoiceItem(input: $input) {
      financeInvoiceItem {
        id
        productName
        description
        quantity
        price
        financeTaxRate {
          id
          name
        }
        total
        lineNumber
      }
    }
  }
`

function FinanceInvoiceEditItems ({ t, history, match, refetchInvoice, inputData }) {
  const [updateItem, { data }] = useMutation(UPDATE_INVOICE_ITEM)

  const onDragEnd = useCallback((result) => {
    // the only one that is required
    console.log('onDragEnd triggered...')
    console.log(result)
    const { draggableId, destination, source, reason } = result
    console.log(source)
    console.log(destination)
    console.log(reason)

    // TODO: notify backend of sorting change
    // dragableID = nodeID 
    // Indexes are 0 indexed
    // source.index = old index
    // destination.index = new index

    // Nothing to do, nowhere to go...
    console.log("drop cancelled...")
    if (!destination || reason === 'CANCEL') {
      return
    }

    // Moved back to the same spot
    console.log("dropped to the same spot")
    if (
      destination.droppableId === source.droppableId &&
      destination.index === source.index
    ) {
      return
    }


    updateLineNumber({
      node_id: draggableId,
      line_number: destination.index
    })

  }, []);


  const updateLineNumber = ({ node_id, line_number }) => {
    updateItem({ 
      variables: { 
        input: {
          id: node_id,
          lineNumber: line_number
        } 
      },
    }).then(({ data }) => {
      console.log('got data', data)
      toast.success((t('settings.general.toast_edit_success')), {
          position: toast.POSITION.BOTTOM_RIGHT
      })
    }).catch((error) => {
      toast.error((t('general.toast_server_error')) + ': ' +  error, {
          position: toast.POSITION.BOTTOM_RIGHT
      })
      console.log('there was an error sending the query', error)
    })
  }

  return (
    <DragDropContext onDragEnd={onDragEnd} >
      <Card statusColor="blue">
        <Card.Header>
          <Card.Title>{t('general.items')}</Card.Title>
          <Card.Options>
            <FinanceInvoiceItemAdd />
          </Card.Options>
        </Card.Header>
        <Card.Body>
          <Table>
            <Table.Header>
              <Table.Row>
                <Table.ColHeader>{t("general.product")}</Table.ColHeader>
                <Table.ColHeader>{t("general.description")}</Table.ColHeader>
                <Table.ColHeader>{t("general.quantity_short_and_price")}</Table.ColHeader>
                <Table.ColHeader>{t("general.tax")}</Table.ColHeader>
                <Table.ColHeader>{t("general.total")}</Table.ColHeader>
                <Table.ColHeader></Table.ColHeader>
              </Table.Row>
            </Table.Header>
            <Droppable droppableId="invoice_items">
              {(provided, snapshot) => (
                  <tbody 
                    ref={provided.innerRef} 
                    {...provided.droppableProps} 
                  >
                    {inputData.financeInvoice.items.edges.map(({ node }, idx) => (
                      <Draggable 
                        draggableId={node.id}
                        index={idx}
                        key={node.id}
                      >
                        {(provided, snapshot) => (
                            <tr 
                              ref={provided.innerRef}
                              {...provided.draggableProps}
                              {...provided.dragHandleProps}
                            >
                              <Table.Col>
                                <UpdateProductName initialValues={node} />
                              </Table.Col>
                              <Table.Col>
                                <UpdateDescription initialValues={node} />
                              </Table.Col>
                              <Table.Col>
                                <UpdateQuantity initialValues={node} />
                                <UpdatePrice initialValues={node} />
                              </Table.Col>
                              <Table.Col>
                                <UpdateFinanceTaxRate initialValues={node} inputData={inputData} />
                              </Table.Col>
                              <Table.Col>
                                <span className="pull-right">{node.totalDisplay}</span>
                              </Table.Col>
                              <Table.Col>
                                <FinanceInvoiceItemDelete node={node} />
                              </Table.Col>
                            </tr>
                        )}
                      </Draggable>
                    ))}
                    {provided.placeholder}
                  </tbody>
              )}
            </Droppable>
          </Table>
        </Card.Body>
      </Card>
    </DragDropContext>
  )
}


export default withTranslation()(withRouter(FinanceInvoiceEditItems))