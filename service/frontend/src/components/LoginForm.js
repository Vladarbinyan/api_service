import {Form, Input, Button} from 'antd';
import React from 'react'


class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {login: '', password: ''}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }


    handleSubmit = (values) => {
        // console.log(values.login, values.password);
        this.props.get_token(values.login, values.password)

    }


    render() {
        return (
            <Form onFinish={this.handleSubmit}>

                <Input.Group>
                    <Form.Item style={{float: 'left'}}
                               label="Username"
                               name="login"
                               rules={[
                                   {
                                       required: true,
                                       message: 'Please input your username!',
                                   },
                               ]} value={this.state.login} onChange={(event) => this.handleChange(event)}>
                        <Input/>
                    </Form.Item>
                    <Form.Item style={{float: 'left'}}
                               label="Password"
                               name="password"
                               rules={[
                                   {
                                       required: true,
                                       message: 'Please input your password!',
                                   },
                               ]} value={this.state.password} onChange={(event) => this.handleChange(event)}>
                        <Input.Password/>
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="submit" value="Login">
                            Login
                        </Button>
                    </Form.Item>
                </Input.Group>
            </Form>
        )
            ;
    }
}

export default LoginForm
