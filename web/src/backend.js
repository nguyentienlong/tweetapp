import axios from 'axios'

let $axios = axios.create({
    baseURL: '/api/',
    port: 8000,
    timeout: 5000,
    headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
    return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
    return response
}, function (error) {
    // Handle Error
    console.log(error)
    return Promise.reject(error)
})

export default {

    getTweet (twitterHandle) {
        console.log('get tweets for ' + twitterHandle)
        return $axios.get('/tweet/'+twitterHandle).then(response => response.data)
    }
}
