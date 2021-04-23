import {Form, Input, Button, Select} from 'antd';
import React from 'react'


class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {todo: '', text: '', user: '', project: ''}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit = (values) => {
        console.log(values);
        // this.props.get_token(values.login, values.password)
    }

    render() {
        return (
            <Form onFinish={this.handleSubmit}>

                <Input.Group>
                    <Form.Item style={{float: 'left'}}
                               label="TODO"
                               name="todo"
                               rules={[
                                   {
                                       required: true,
                                       message: 'Please input TODO title',
                                   },
                               ]}>
                        <Input/>
                    </Form.Item>
                    <Form.Item style={{float: 'left'}} label="Project" name="project">
                        <Select >{this.props.projects.map((project)=><option value={project.uuid}>{project.uuid}</option>)}</Select>
                    </Form.Item>
                    <Form.Item style={{float: 'left'}}
                               label="Text"
                               name="text"
                    >
                        <Input.Password/>
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="submit">
                            Post data
                        </Button>
                    </Form.Item>
                </Input.Group>
            </Form>
        );
    }
}

export default TodoForm
