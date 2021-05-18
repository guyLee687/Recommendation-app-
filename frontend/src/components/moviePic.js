import React from 'react';
import AddFavorite from './AddFavorite'

//Compoment takes in the image of the movie, the title and the link to where
// the image is stored. 
const moviePic = ({movie}) => {
    let list1 = localStorage.getItem('movie-favorites');
    let favorites = [];
    if(list1)
        favorites = JSON.parse(list1);

    let list2 = localStorage.getItem('movie-watched');
    let watched = [];
    if(list2)
        watched = JSON.parse(list2);

    return (
        <div className='MovieFrame justify-content-start centerThis'>            
            <img src={movie.link} alt={movie.name + " picture"}></img>
            <div className="overlay align-items-center justify-content-center">
                <AddFavorite movie={movie} 
                isFavorited={favorites.find((ele) => movie.name === ele.name) ? true : false}
                isWatched={watched.find((ele) => movie.name === ele.name) ? true : false}/>
            </div>
        </div>
    )
}

moviePic.defaultProps = {
    text: "A movie picture"
}

export default moviePic
