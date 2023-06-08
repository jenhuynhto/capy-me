// mycomponent.js
const MyComponent = {
    template: `
      <div>
        <h1>Hello, {{ name }}!</h1>
        <button @click="increment">Click me</button>
      </div>
    `,
    data() {
      return {
        name: 'Vue',
      };
    },
    methods: {
      increment() {
        this.name += '!';
      },
    },
  };
  
  // Mount the component to an element
  new Vue({
    el: '#app',
    components: {
      MyComponent,
    },
  });