import React from 'react';
import {Layout, Menu, Table} from "antd";

const {Header} = Layout;


const MainMenu = ({selected_key}) => {
    return (
        <Header>
            <Menu theme="dark" mode="horizontal" defaultSelectedKeys={[selected_key]}>
                <Menu.Item key="1">Users</Menu.Item>
                <Menu.Item key="2">Help</Menu.Item>
            </Menu>
        </Header>
    )
}

export default MainMenu

