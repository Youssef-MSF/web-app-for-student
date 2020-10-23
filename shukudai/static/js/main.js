const dashboard = new Vue({
    el: '.main',
    data: {
        title: 'For Students',
        selectedFromMenu: 'Dashboard'
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