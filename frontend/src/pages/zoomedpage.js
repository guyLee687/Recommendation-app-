import {useState, useEffect} from 'react';
import Movies from "../components/moviePic"
import Header from "../components/header"
import Summary from "../components/summary"
import SimilarMovies from "../components/similarMovies"
import Rating from "../components/review"
import MyNav from '../components/navbar'
import {AppContext} from '../AppContext';
import {Container, Row, Col} from 'react-bootstrap'
import './zoomed-paged-grid.css';

function ZoomedPage() {
  const database_address = "http://localhost:4000/movies";
  const [showMovie, setMovie] = useState ([{"id": 0,
  "title": "",
  "picture": "",
  "Rating": "",
  "text": "" }]);
  const [simShowMovies, setSimMovies] = useState ([{"id": 0,
  "title": "",
  "picture": "",
  "Rating": "",
  "text": "" }]);


  //Updates movies on effect
  useEffect(() => {
    const id = Math.floor(Math.random() * 20) + 1
    const getMovies = async () => {
      const movieFromServer = await fetchMovies(id)
      setMovie(movieFromServer)
    }
    getMovies();
    getSimMovies(id)
  }, [])

    //Fetches similar movies from database
    const getSimMovies = async (id) => {
      await setSimMovies(0)
      //Substitute with backend call for similar movies.
      const movies = 9; // Show 3 recommended movies
      let temp_id = id;
      for (let i = 0; i < movies; i++) {
        temp_id = ((++temp_id) % 20) + 1
        const movieFromServer = await fetchMovies(temp_id);
        console.log(movieFromServer[0])
        await setSimMovies([...simShowMovies, movieFromServer[0]])
      }
      console.log(simShowMovies)
    }

    //Fetches individual movie from database
    const fetchMovies = async (id) => {
      const response = await fetch(database_address + `?id=${id}`)
      const data = await response.json()

      return data
    }


    return(
      <AppContext.Consumer>
        {context => <>
          <MyNav />
          <Container fluid>
            <Row>
              <Col ><Movies movie={[context.movie]}/></Col>
              <Col md={5} lg={9}>
                <Row className="MovieTitle">
                  <Header movie={[context.movie]}/>
                </Row>
                <Row className="Ratings">
                  <Rating movie={[context.movie]} />
                </Row>
                <Row className="Summary">
                  <Summary movie={[context.movie]}/>
                </Row>
              </Col>
            </Row>
            <Row>
              <Col md= {3}></Col>
              <Col className="SimilarMovies">
               <SimilarMovies />
              </Col>
            </Row>
          </Container>
        </>}
      </AppContext.Consumer>
  );
}

export default ZoomedPage;

{/* <div className="zoom-container">
<div className="titleNav">
  .
</div>
<div className="MoviePic">
  <Movies movie={[context.movie]}/>
</div>
<div className="SimilarMovies">
  <SimilarMovies />
</div>
<div className="MovieTitle">
  <Header movie={[context.movie]}/>
</div>
<div className="Ratings">
  <Rating movie={[context.movie]} />
</div>
<div className="Summary">
  <Summary movie={[context.movie]}/>
</div>

</div> */}