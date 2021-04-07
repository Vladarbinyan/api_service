import React from "react";
import User from "./components/User";
import TextFooter from "./components/TextFooter";
import MainMenu from "./components/Menu";
import PageNotFound from "./components/PageNotFound";
import Project from "./components/Project";
import Todo from "./components/Todo";
import axios from "axios";
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'


const DOMAIN = 'http://127.0.0.1:8000'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todo': [],
        }
    }

    async componentDidMount() {
        await axios.get(get_url('/api/users/'))
            .then(response => {
                    console.log(response.data)
                    const users = response.data
                    this.setState(
                        {
                            'users': users.results,
                        }
                    )
                }
            ).catch(error => console.log(error))
        await axios.get(get_url('/api/projects/'))
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects.results
                    }
                )
            }).catch(error => console.log(error))

        await axios.get(get_url('/api/todo/'))
            .then(response => {
                const todo = response.data
                this.setState(
                    {
                        'todo': todo.results
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <div>
                        <MainMenu selected_key={"1"}/>
                    </div>
                    <Switch>
                        <Route exact path='/' component={() => <User users={this.state.users}/>}/>
                        <Route exact path='/users' component={() => <User users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <Project projects={this.state.projects}/>}/>
                        <Route exact path='/todo' component={() => <Todo todo={this.state.todo}/>}/>
                        <Route component={PageNotFound}/>
                    </Switch>
                    <div>
                        <TextFooter footer='API SERVICE 2021'/>
                    </div>
                </BrowserRouter>
            </div>

            // <div>

            // </div>
        )
    }
}

export default App

