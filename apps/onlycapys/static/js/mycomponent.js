// This will be the object that will contain the Vue attributes
// and be used to initialize it.

// Given an empty app object, initializes it filling its attributes,
// creates a Vue instance, and then initializes the Vue instance.
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
      a.map((e) => {e._idx = k++;});
      return a;
  };    

  
  // This contains all the methods.
  self.methods = {
      // Complete as you see fit.
  };
  selftoggle= function(){
    
  }
  // This creates the Vue instance.
  self.vue = new Vue({
      el: "#vue-target",
      data: self.data,
      methods: self.methods
  });

  self.init = () => {
    // Put here any initialization code.
   
    axios.get(get_capyfacts_url).then(function (response) {
      self.vue.facts = self.enumerate(response.data.facts);
      console.log("self.vue.facts: ", self.vue.facts);
    });
};
  self.init();
  // Put here any initialization code.
  console.log("self.vue.facts")
  return self;
};

// This takes the (empty) app object, and initializes it,
// putting all the code in it. 
var app = init();
