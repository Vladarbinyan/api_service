import React from 'react';
import { Layout, Menu} from "antd";
import {Link} from "react-router-dom";

const {Header} = Layout;


class MainMenu extends React.Component {


    logout() {
        this.props.logout()
    }

    render() {
        return (
            <Header>
                <Menu theme="dark" mode="horizontal" defaultSelectedKeys={this.props.default_key}>
                    <Menu.Item key="1"><Link to='/users'>Users</Link></Menu.Item>
                    <Menu.Item key="2"><Link to='/projects'>Projects</Link></Menu.Item>
                    <Menu.Item key="3"><Link to='/todo'>TODO</Link></Menu.Item>
                    <Menu.Item style={{float: 'right'}} key="4">{this.props.is_authenticated ?
                        <Link onClick={() => this.logout()}>Logout</Link> :
                        <Link to='/login'>Login</Link>}
                    </Menu.Item>


                </Menu>
            </Header>
        );
    }
}

export default MainMenu

