'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
    constructor(props) {
    super(props);
    // this.state = {count: 0};
    this.state = props.count;
  }


  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  decrement = () => {
      if (this.state.count >0) {
            this.setState({ count: this.state.count - 1 });
      }
      else {
          this.setState({ count: this.state.count })
      }
  };

  render() {
    return (

      <div>
      <p> Count: {this.state.count}</p>
      <button onClick={this.increment}>Increment</button>

      <button onClick={this.decrement}>Decrement</button>
      </div>
    );
  };
}
const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);