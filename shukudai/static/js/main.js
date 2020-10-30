const dashboard = new Vue({
    el: '.main',
    data() {
    return {
        range: {
            start: new Date(2020, 0, 1),
            end: new Date(2020, 0, 5)
        }
    }
},
    methods: {
        changeMenu: function(selected) {
            this.selectedFromMenu = selected;
        }
    },
    mounted() {
        document.getElementById("today").innerHTML = Date().split(' ')[2] + ' ' + Date().split(' ')[1] + ' ' + Date().split(' ')[3] + ' , ' + Date().split(' ')[0];
    }
});

const homePage = new Vue({
    el: '.home-page',
    data: {
        title: 'Built for students'
    }
});

const forum = new Vue({
    el: '.forum-container',
    data: {
        showMenu: false
    },
    methods: {
        expandMenu: function() {
            this.showMenu = !this.showMenu
        }
    }
});


const app = new Vue({
    el: '.email-password-login',
    components: {
        vuejsDatepicker
    }
});

const smthng = new Vue({
    el: '#calendar',
    components: {
        vuejsDatepicker
    }
});