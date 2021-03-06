import React from "react";
import {Layout} from 'antd';
import UserList from "./components/User";
import TextFooter from "./components/TextFooter";
import MainMenu from "./components/Menu";
import axios from "axios";
import * as url from "url";


const {Content} = Layout;


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                    const users = response.data
                    this.setState(
                        {
                            'users': users,
                        }
                    )
                }
            ).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <div>
                    <MainMenu selected_key={"1"}/>
                </div>
                <div>
                    <UserList users={this.state.users}/>
                </div>
                <div>
                    <TextFooter footer='API SERVICE 2021'/>
                </div>
            </div>
        )
    }
}

export default App

