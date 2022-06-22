import { Button, Checkbox, List, Col, Input, Pagination } from 'antd';
import React, {Component } from 'react';

export default class Todo extends Component {

    state = {
        todoList: [],
        currentPage : 1,
        perPage : 10,
    }

    componentDidMount() {
        fetch('https://jsonplaceholder.typicode.com/todos')
        .then(res => res.json())
        .then(res => this.setState({todoList : res}))
    }
    
    handelerTodoChecked = (todoID) => {
        let todo = JSON.parse(JSON.stringify(this.state.todoList))

        todo = todo.filter((item) => {
            if(item.id === todoID) {
                item.completed = !item.completed
            }
            return item;
        })
        this.setState({todoList : todo})
    }

    handlerDeleteTodo = (todoID) => {
        let todo = JSON.parse(JSON.stringify(this.state.todoList))

        todo = todo.filter((item) => {
            if (item.id !== todoID) return item;
            else return undefined;
        })
        this.setState({todoList : todo})
    }

    handlerAddToTodo =(e) => {
        console.log(e)
        let defVariable = [{id: Math.random(), title:e.target.value, completed: false}]
        this.setState({todoList : [...this.state.todoList, ...defVariable] })
    }

    handlerUpdatePages = (page, pageSize) => {
        this.setState({currentPage: page ? page : 1, perPage: pageSize});
    }

    render(){
        const {todoList} = this.state;
        const {currentPage} = this.state;
        const {perPage} = this.state;

        const firstItem = (currentPage - 1) * perPage;
        const lastItem = currentPage * perPage;
        const todoPageList = todoList.slice(firstItem, lastItem);

        return(
            <>
                <Col span={8} style={{margin: '0 auto'}}>
                    <h3>My todo list</h3>
                    <List>
                        <Input placeholder='Добавить todo в список' onPressEnter={(e) => this.handlerAddToTodo(e)}/>
                        {todoPageList.map((item, index)=>{
                            return(          
                                <List.Item key={index} style={{listStyle: 'decimal', textDecoration : item.completed ? 'line-through' : 'none', display: 'flex'}} >
                                    <div>
                                        <Checkbox onChange={() => this.handelerTodoChecked(item.id) } checked={item.completed ? true : false } style={{marginRight: 16}}/>
                                        <span>{item.title}</span>
                                    </div>
                                    <Button onClick={()=> this.handlerDeleteTodo(item.id) }>Удалить</Button>
                                </List.Item>
                            )
                        })}
                    </List>
                    <Pagination size="small" showSizeChanger showQuickJumper defaultCurrent={currentPage} defaultPageSize={perPage} total={todoList.length} onChange={this.handlerUpdatePages} style={{paddingBottom: 16}} />
                </Col>
            </>
        )
    }
}