import React from "react";
import './App.css';
import UserList from "./components/User";
import axios from "axios";
import * as url from "url";
import {Layout, } from "antd";

const { Header, Footer, Content } = Layout;

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                    const users = response.data
                    this.setState(
                        {
                            'users': users
                        }
                    )
                }
            ).catch(error => console.log(error))
    }

    render() {
        return (
            <Layout>
                <Header>Menu</Header>
                <Content>
                    <div>
                        <UserList users={this.state.users}/>
                    </div>
                </Content>
                <Footer>Footer</Footer>
            </Layout>
        )
    }
}

export default App

