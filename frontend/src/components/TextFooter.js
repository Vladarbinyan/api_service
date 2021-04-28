import React from 'react';
import {Layout} from "antd";
const {Footer} = Layout;

const TextFooter = ({footer}) => {
    return (
        <Footer style={{textAlign: 'center'}}>
                <div className='footer'>{footer}</div>
        </Footer>
    )
}

export default TextFooter;