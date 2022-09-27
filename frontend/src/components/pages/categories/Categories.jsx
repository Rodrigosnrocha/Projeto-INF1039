import './Categories.css'
import { Component } from 'react'
import { Link } from 'react-router-dom'
import Main from '../../templates/Main'
import PlaceBox from '../../place/PlaceBox'
import imagemRdc from '../../../assets/rdc-lugar.jpg'

export default class Categories extends Component {

  state = {
    places: [],
    word: ''
  }

  constructor(props) {
    super(props)
    this.fillField = this.fillField.bind(this)
    this.wordSearchPlace = this.wordSearchPlace.bind(this)
  }

  // Funciona no vscode
  componentDidMount() {
    fetch('http://127.0.0.1:8000/api/lugar/')
      .then(resp => resp.json())
      .then(places => this.setState({ places }))
  }

  fillField(e) {
    const field = { ...this.state }
    field[e.target.name] = e.target.value
    this.setState(field)
}

  wordSearchPlace(e) {
    e.preventDefault()
    fetch(`http://127.0.0.1:8000/api/lugar/?titulo__contains=${this.state.word}`)
      .then(resp => resp.json())
      .then(places => this.setState({ places }))
  }

  renderPlaces() {
    return this.state.places.map(place => {
      return (
        <PlaceBox key={place.id} 
          titulo={place.titulo} descricao={place.descricao} autor={place.autor} thumb={place.thumb}
          tags={place.tags} likes_count={place.likes_count} dislikes_count={place.dislikes_count}/>
      )
    })
  }
  
  render() {
    return (
      <Main>
        <h1 className='display-4'>
          Categorias
        </h1>
        <hr />
        <div className='d-flex align-items-center mb-4'>
          <Link to="/registrarLugar" className="btn btn-secondary" role="button">
            Criar Lugar
          </Link>
          <form className='search form m-0' onSubmit={this.wordSearchPlace}>
            <div className="form-items form-group d-flex justify-content-between mx-5">
              <input type="text" name='word' onChange={this.fillField} value={this.state.word} className="form-control input-sm mx-2" id="place" placeholder="Nome do Lugar" />
              <button type="submit" className="btn btn-primary py-0 px-2 ml-2">Pesquisar</button>
            </div>
          </form>
        </div>
        <div>
          {this.renderPlaces()}
        </div>
        <div> 
          <img className='img-fluid' src={imagemRdc} alt='Início' />
        </div>
      </Main>
    )
  }
}