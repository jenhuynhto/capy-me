let init = function () {
  var self = {};

  // This is the Vue data.
  self.data = {
    facts: [],
    // Complete as you see fit.
  };

  self.enumerate = function (a) {
    // This adds an _idx field to each element of the array.
    let k = 0;
    a.map((e) => {
      e._idx = k++;
    });
    return a;
  };

  // This contains all the methods.
  self.methods = {
    
  };

  // This creates the Vue instance.
  self.vue = new Vue({
    el: "#vue-target",
    data: self.data,
    methods: self.methods,
  });

  self.init = () => {
    // Put here any initialization code.
    axios.get(get_capyfacts_url).then(function (response) {
      self.vue.facts = self.enumerate(response.data.facts);
    });
    
  };

  self.init();
  // Put here any initialization code.

  return self;
};

// This takes the (empty) app object, and initializes it,
// putting all the code in it.
var app = init();
