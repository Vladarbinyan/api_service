import React from "react";
import User from "./components/User";
import TextFooter from "./components/TextFooter";
import MainMenu from "./components/Menu";
import PageNotFound from "./components/PageNotFound";
import Project from "./components/Project";
import Todo from "./components/Todo";
import LoginForm from "./components/LoginForm";
import axios from "axios";
import {BrowserRouter, Route, Switch} from 'react-router-dom'
import Cookies from 'universal-cookie';


const DOMAIN = 'http://127.0.0.1:8000'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props);
        this.logout = this.logout.bind(this);
        this.state = {
            'users': [],
            'projects': [],
            'todo': [],
            'token': '',
            'username': '',
        }
    }

    set_token(token, username) {
        const cookies = new Cookies()
        cookies.set('token', token)
        cookies.set('username', username)
        this.setState({'token': token, 'username': username}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('', '')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const username = cookies.get('username')
        this.setState({'token': token, 'username': username}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post(get_url('/api-token-auth/'), {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'], username)
            }).catch(error => alert('Bad login or password!'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


    load_data() {
        const headers = this.get_headers()
        axios.get(get_url('/api/users/'), {headers})
            .then(response => {
                this.setState({'users': response.data.results})
            }).catch(error => {console.log(error)
            this.setState({'users': []})
            })

        axios.get(get_url('/api/projects/'), {headers})
            .then(response => {
                this.setState({'projects': response.data.results})
            }).catch(error => {console.log(error)
            this.setState({'projects': []})
            })

        axios.get(get_url('/api/todo/'), {headers})
            .then(response => {
                this.setState({'todo': response.data.results})
            }).catch(error => {console.log(error)
            this.setState({'todo': []})
            })


    }


    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <div>
                        <MainMenu default_key={"1"} is_authenticated={this.is_authenticated()} logout={this.logout} username={this.state.username}/>
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

