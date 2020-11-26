import React from "react";
import "./App.css";

function Footer(props) {
  return (
    <footer>
      <small>hi there</small>
      <span>props say ... {props.message}</span>
    </footer>
  );
}
export default function App() {
  return (
    <>
      <main>
        <div className="App">
          <h1>Woohoo</h1>
        </div>
        <MoodRing />
      </main>
      <Footer message="hi from outside" />
    </>
  );
  }

class MoodRing extends React.Component {

    constructor() {
        super();
        this.state = {
            mood : 'neutral',
        }
    }

    changeMood(change) {

        let newMood = '';

        if (change === 'improve') {

            if (this.state.mood === 'sad') {
                newMood = 'neutral';
            } else {
                newMood = 'happy';
            }

        } else {

            if (this.state.mood === 'happy') {
                newMood = 'neutral';
            } else {
                newMood = 'sad';
            }

        }

        this.setState({
            mood : newMood,
        });
    }

    render() {
        return (
            <>
            <button onClick={() => this.changeMood("improve")}>improve</button>
            <button onClick={() => this.changeMood("worsen")}>worsen</button>
            <h2>Mood Ring says... {this.state.mood}</h2>
            </>
        )
    }

}




  // return (
  //   <div className="App">
  //     <h1>Hello CodeSandbox {getMood()}</h1>
  //     <h2>Start editing to see some magic happen!</h2>
  //   </div>
  // );
// }

// const getMood = function() {
//   return "sad";
// };

// getMood();

// function getMood() {
//   return "elated";
// }
