import React, { useEffect, useState } from 'react'


import axios from 'axios'

//import { Container } from 'react-bootstrap'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'

import { Link } from 'react-router-dom'

const Home = () => {
  const [continents, setContinents] = useState([])

  useEffect(() => {
    const getContinents = async () => {
      const { data } = await axios.get('/api/continents/')
      setContinents(data)
    }
    getContinents()
  }, [])

  return (
    <div className="site-wrapper">
      <div className="text-center">
        <div className="background-image">
          <h2 className="display-2">🐴 Horse Outdoors 🐎</h2>
          <h4>Discover new scenery for your horse riding vacations.</h4>
          <p>Start your journey by choosing a continent</p>
        </div>
        <div className="continent-cards mb-3">
          {continents.length ? continents.map(continent => {
            // return <Card className="h-100" key={continent.id} to={`destinations/${continent.id}`} className='continent-card'>{continent.name}
            // </Card>
            return <Row key={continent.id} xs={1} md={4} className="continents mb-4">
              {Array.from({ length: 1 }).map((_, idx) => (
                <Col>
                  <Link to={`destinations/${continent.id}`}>
                    <Card className="continent-card" >
                      <Card.Img variant="bottom" src={continent.image} />
                      <Card.Body>
                        <Card.Footer className="text-center">
                          {continent.name}
                        </Card.Footer>
                      </Card.Body>
                    </Card>
                  </Link>
                </Col>
              ))}
            </Row>
          }) : ''}
        </div>
      </div>
    </div>
  )
}

export default Home