/*
 * Objects to implement a client-side post database.
 */
function escape(message) {
    var reg = /<\s*script[^>]*>[\s\S]*?<\s*\/\s*script\s*>/gi;

    if (reg.test(message)) {
        return true;
    }

    var key = ['script', 'eval', 'alert', 'prompt', 'confirm'];
    for (var i = 0; i < key.length; i++) {
        var word = key[i];
        var pattern = new RegExp(word, 'i');
        if (pattern.test(message)) {
            return true;
        }
    }

    return false;
}

function Post(message) {
    if(escape(message)){
        this.message = ''
    }else{
          this.message = (message);
    }

  this.date = (new Date()).getTime();
}

function PostDB(defaultMessage) {
  // Initial message to display to users
  this._defaultMessage = defaultMessage || "";

  this.setup = function() {
    var defaultPost = new Post(defaultMessage);
    window.localStorage["postDB"] = JSON.stringify({
      "posts" : [defaultPost]
    });
  }

  this.save = function(message, callback) {
    var newPost = new Post(message);
    var allPosts = this.getPosts();
    allPosts.push(newPost);
    window.localStorage["postDB"] = JSON.stringify({
      "posts" : allPosts
    });

    callback();
    return false;
  }

  this.clear = function(callback) {
    this.setup();

    callback();
    return false;
  }

  this.getPosts = function() {
    return JSON.parse(window.localStorage["postDB"]).posts;
  }

  if(!window.localStorage["postDB"]) {
    this.setup();
  }
}