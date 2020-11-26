import React from 'react';
import './App.css';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            snacks : [
                {
                    id: 1,
                    name: 'apple',
                    category: 'fruit',
                },
                {
                    id: 2,
                    name: 'snickers',
                    category: 'candy',
                }

            ],
            latestSnack: null
        }

        this.snackCreatedHandler = this.snackCreatedHandler.bind(this);

        this.state.latestSnack = this.state.snacks[this.state.snacks.length - 1];

    }

    snackCreatedHandler(snack) {

        const updatedSnacks = this.state.snacks;

        updatedSnacks.push({name:snack.name,type:"???",id:Math.floor(Math.random() * 10000)}) // WARNING: random just for now

        this.setState({
            snacks : updatedSnacks,
            latestSnack : snack
        })
    }

    render() {
        return (
        <div className="App">
            <Header latestSnack={this.state.latestSnack} />
            <main>
                <SnackList snacks={this.state.snacks} />
                {/* Note the lab may want the form in different location */}
                <SnackForm onSnackCreateKiwi={this.snackCreatedHandler} otherStuff="whatever" />
            </main>
            <Footer text="whatever" />
        </div>
        )
    }

}

function SnackList(props) {

    // need a function to call when creating a new thing
    // function should be in props

    return (
        <>
        <h2>Snacks</h2>
        <ul>
           {props.snacks.map(snack => <Snack item={snack} key={snack.id} />)}
        </ul>
        </>

    )
}

class SnackForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            name : '???',
            category: '???',
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {

        if(event.target.name === "snack-name") {
            const newName = event.target.value;
            this.setState({
                name: newName,
            })
        } else { // must be snack-category
            const newCategory = event.target.value;
            this.setState({
                category: newCategory
            })
        }
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.onSnackCreateKiwi(this.state);
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Name:
                    <input
                    name="snack-name" type="text" value={this.state.name} onChange={this.handleChange}>
                    </input>
                </label>
                <label>
                    Category:
                    <input
                    name="snack-category" type="text" value={this.state.category} onChange={this.handleChange}>
                    </input>
                </label>
                <button>ok</button>
            </form>
        )
    }
}

function Snack(props) {
    return <li>I am snack {props.item.name} and I am {props.item.category}</li>
}


function Header(props) {

    return <h2>Popular snack is {props.latestSnack.name}, {props.latestSnack.category}</h2>
}

function Footer(props) {
    return <footer><small>{props.text}</small></footer>
}

export default App;
