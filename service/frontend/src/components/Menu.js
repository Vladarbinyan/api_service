import React from 'react';
import {Layout, Menu} from "antd";
import {Link} from "react-router-dom";

const {Header} = Layout;


const MainMenu = ({selected_key}) => {
    return (
        <Header>
            <Menu theme="dark" mode="horizontal" defaultSelectedKeys={[selected_key]}>
                <Menu.Item key="1"><Link to='/users'>Users</Link></Menu.Item>
                <Menu.Item key="2"><Link to='/projects'>Projects</Link></Menu.Item>
                <Menu.Item key="3"><Link to='/todo'>"TODO"</Link></Menu.Item>
            </Menu>
        </Header>
    )
}

export default MainMenu

