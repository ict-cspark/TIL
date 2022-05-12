# 사전준비

### 1. CDN 작성

```html
<body>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</body>
```



### 2. Vue 인스턴스

```html
<script>
    const app = new Vue({
        el: '#app',
        data: {
            message: 'Hello',
    	},
        methods: {
            greeting: function (){
                console.log('hello')
            }
        },
  	})
</script>
```



### 2-1. Vue Syntax

```html
<body>
    <div id="app">
        // v-text
    	<p v-text="message"></p>
    
    	// v-show
    	<p v-show="isTrue"></p>
    
    	// v-if, v-else-if, v-else
        <div v-if="myType === 'A'"></div>
        <div v-else-if="myType === 'B'"></div>
        <div v-else></div>
        
        // v-for
        <div v-for="(todo, idx) in todos" :key="idx"></div>
        
        // v-on
        <button @click="doAlert">Button</button>
        
        // v-bind
        <div :class="{ active: isRed }"></div>
        
        // v-model
        <input v-model="message" type="text">       
    </div>
    
    <script>
    	// computed
        computed: {
            doubleNum: function(){
                return this.num * 2
            }
        },
            
        // filter
        filters: {
            getOddNums: function (nums){
                const oddNums = nums.filter(function (num) {
                    return num % 2
                })
                return oddNums
            },
        },
            
        // created
        created: function(){
            this.getImg()
        },
    </script>
</body>
```



### 3. Vue CLI

```bash
# 설치
$ npm install -g @vue/cli

# 버전 확인
$ vue --version

# 프로젝트 생성
$ vue create my-frist-app

# 프로젝트 이동 및 서버 실행
$ cd my-frist-app
$ npm run serve
```



### 3-1. Vue 패키지 설치

```bash
# node_modules 설치
$ npm install


# lodash 설치 및 import
$ npm install lodash
import _ from "lodash"


# axios 설치 및 import
$ npm install axios
import axios from 'axios'


# localstorage 설치 및 설정
$ npm install vuex-persistedstate

// index.js
import createPersistedState from 'vuex-persistedstate'

export default {
	plugins: [
		createPersistedState(),
	],
}
```



---

## Props & Emit

```vue
// App.vue

<template>
	<div id="app">
        <p>{{ childData }}</p>		// emit
        <child-app :parent-data="parentData" @child-input-data="childGetData"></child-app>
    </div>
</template>

<script>
import childApp from '@/components/childApp.vue'
    
export default {
    name: 'App',
    components: {
        childApp,
    },
    data: function(){
        return {
            parentData: 'parentData',	// props
            childData: 'childData',		// emit
        }
    },
    methods: {
        childGetData: function(data) {	// emit
            this.childData = data
        }
    }
}
</script>

<style>
</style>
```

```vue
// childApp.vue

<template>
	<div id="app">
        <p>{{ parentData }}</p>	// props
        <input @keyup.enter="childInputData" type="text" v-model.trim="childData">
    </div>
</template>

<script>
export default {
    name: 'childApp',
    props: {					// props
        paretndData: {
            type: String,
        },
    },
    data: function(){
        return {
            childData: null,	// emit
        }
    },
    methods: {
        childInputData: function() {
            this.$emit('child-input-data', this.childData)	// emit
        },
    },
}
</script>

<style>
</style>
```



---

## Router

#### 1. 사전준비

```bash
$ vue create my-router-app
$ cd my-router-app

// Vue Router plugin 서리
$ vue add router

$ npm run serve
```



#### index.js

```javascript
Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about/:aboutId'
        name: 'about'
        componete: about
    },
]
```



#### App.vue

```html
<template>
    <div id="app">
       <nav>
           <router-link to="/">Home</router-link> |
           <router-link :to="{ name: 'about', params: { aboutId }}">About</router-link>
       </nav>
       <router-view/>
    </div>
</template>
```



#### About.vue

```html
<template>
    <div id="app">
       <h1>About</h1>
       <h4>{{ $route.params.aboutId }}</h4>			// Dynamic Route Matching
       <button @click="moveHome">Home</button>
    </div>
</template>

<script>
export default {
    name: 'About',
    methods: {
        moveHome: function(){
            this.$router.push({ name: 'home' })		// 프로그래밍 방식 내비게이션
        }
    },
}
</script>
```



---

## Vuex

#### 1. 사전준비

```bash
$ vue create todo-vuex-app
$ cd todo-vuex-app

$ vue add vuex

import vuex from 'vuex'
```



#### 데이터 가져오기

```vue
<template>
  <div>
    <todo-list-item
    v-for="(todo, idx) in todos"
    :key="idx"
    :todo="todo"
    >
    </todo-list-item>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  computed: {
    todos: function(){
        return this.$store.state.todos
    }
  },
}
```



#### Vuex 상태 관리 흐름

```javascript
// Components -> Dispatch -> Actions

this.$store.dispatch('createTodo', todoItem)

// Actions -> commit -> Mutations
actions: {
    createTodo: function({ commit }, todoItem) {
        commit('CREATE_TODO', todoItem)
    },
},
    
// Mutations -> State
mutations: {
    CREATE_TODO: function(state, todoItem) {
        state.todos.push(todoItem)
        
        const index = state.todos.indexOf(todoItem)
        state.todos.splice(index, 1)
    }
}
```



#### Component Binding Helper

```vue
<template>
  <div id="app">
      ...
    <h3>All Todos: {{allTodos}}</h3>
    <h3>Completed Todo: {{completedTodo}}</h3>
    <h3>Uncompleted Todo: {{uncompletedTodo}}</h3>
	...
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
    
export default {
  name: 'App',
    ...
  computed: {
    ...mapGetters([
      'completedTodo',
      'uncompletedTodo',
      'allTodos',
    ])
  },
}
</script>

```

