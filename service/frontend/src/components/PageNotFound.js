import React from 'react';
import {Layout} from "antd";
const {Content} = Layout;

const PageNotFound = ({location}) => {
    return (
        <Content style={{textAlign: 'center'}}>
                <div>Page '{location.pathname}' not found!</div>
        </Content>
    )
}

export default PageNotFound;