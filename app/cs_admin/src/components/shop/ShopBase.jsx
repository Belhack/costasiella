import React from 'react'
import { withTranslation } from 'react-i18next'
import { withRouter } from "react-router"
import { Link } from 'react-router-dom'

import {
  Page,
  Grid,
  Icon,
  Container,
} from "tabler-react";
import SiteWrapperShop from "../SiteWrapperShop"


function ShopBase({ t, match, history, children, title, return_url }) {

  return (
    <SiteWrapperShop>
      <div className="my-3 my-md-5">
        <Container>
          <Page.Header title={title}>
            <div className="page-options d-flex">
              {/* Back */}
              {(return_url) ?
                <Link to={return_url} 
                      className='btn btn-secondary mr-2'>
                    <Icon prefix="fe" name="arrow-left" /> {t('general.back')} 
                </Link>
                : ""
              }
            </div>
          </Page.Header>
            <Grid.Row>
              <Grid.Col md={12}>
                { children }
              </Grid.Col>
            </Grid.Row>
          </Container>
        </div>
    </SiteWrapperShop>
  )
}


export default withTranslation()(withRouter(ShopBase))