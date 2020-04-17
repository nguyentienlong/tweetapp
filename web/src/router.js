import Vue from 'vue'
import Router from 'vue-router'
import Tweet from './components/Tweet'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'tweet',
            component: Tweet
        }
    ]
})
