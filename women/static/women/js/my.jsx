'use strict';

const e = React.createElement;


class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };

  }

  render() {
    if (this.state.liked) {

      return(
          <div>
          <b> 'You liked this. ' </b>
          <b> {this.state.liked} </b>
          </div>
    )
    }

  // Отображение кнопки "Like"
  return (
    <button onClick={() => this.setState({ liked: true })}>
      <div className="btn-success btn-lg"> Like </div>
    </button>
  );

  }

}
const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);