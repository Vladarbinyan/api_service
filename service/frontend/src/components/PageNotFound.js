import React from 'react';
import {Layout} from "antd";
const {Content} = Layout;

const PageNotFound = ({location}) => {
    return (
        <Content style={{textAlign: 'center'}}>
                <h1>Page '{location.pathname}' not found!</h1>
        </Content>
    )
}

export default PageNotFound;