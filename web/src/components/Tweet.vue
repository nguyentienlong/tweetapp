<template>
  <div>
    <div class="row">
      <div class="col">
        <input v-model="twitterHandle" placeholder="input a twitter handle">
        <button v-on:click="getTweet">Get Tweets</button>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <ul class="list-group">
          <li class="list-group-item" v-for="tweet in tweets" v-bind:key="tweet">
            {{ tweet }}
          </li>
        </ul>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <span class="text-danger">{{error}}</span>
      </div>
    </div>
  </div>
</template>

<script>
    import $backend from '../backend'

    export default {
      name: 'Tweet',
      data () {
          return {
              twitterHandle: '',
              tweets: [],
              error: ''
          }
      },
      created () {
          console.log("created")
      },
      methods: {
          getTweet () {
              if (this.error !== '') {
                  this.error = ''
              }
              if (this.tweets.length > 0) {
                  this.tweets = []
              }
              if (this.twitterHandle.trim() == '') {
                  console.log(this.twitterHandle)
                  this.error = 'Please input a twitter handle'
                  return
              }
              $backend.getTweet(this.twitterHandle).then(responseData => {
                  if (responseData.data.tweets.length > 0) {
                    this.tweets = responseData.data.tweets
                  } else {
                    this.error = 'No tweet found'
                  }
              }).catch(error => {
                  console.log(error)
                  this.error = error.response.data.message
              })
          }
      }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
