import React from "react";
import User from "./components/User";
import TextFooter from "./components/TextFooter";
import MainMenu from "./components/Menu";
import PageNotFound from "./components/PageNotFound";
import Project from "./components/Project";
import Todo from "./components/Todo";
import LoginForm from "./components/Auth";
import axios from "axios";
import {BrowserRouter, Route, Link, Switch} from 'react-router-dom'
import Cookies from 'universal-cookie';


const DOMAIN = 'http://127.0.0.1:8000'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todo': [],
            'token': '',
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }

    get_token(username, password) {
        axios.post(get_url('/api-token-auth/'), {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Bad login or password!'))
    }

    load_data() {
        axios.get(get_url('/api/users/'))
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

        axios.get(get_url('/api/projects/'))
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects.results
                    }
                )
            }).catch(error => console.log(error))

        axios.get(get_url('/api/todo/'))
            .then(response => {
                const todo = response.data
                this.setState(
                    {
                        'todo': todo.results
                    }
                )
            }).catch(error => console.log(error))

    }


    async componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <div>
                        <MainMenu selected_key={"1"}/>
                    </div>
                    <Switch>
                        <Route exact path='/' component={() => <User users={this.state.users}/>}/>
                        <Route exact path='/users' component={() => <User users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <Project projects={this.state.projects}/>}/>
                        <Route exact path='/todo' component={() => <Todo todo={this.state.todo}/>}/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route component={PageNotFound}/>
                    </Switch>
                    <div>
                        <TextFooter footer='API SERVICE 2021'/>
                    </div>
                </BrowserRouter>
            </div>
        )
    }
}

export default App

