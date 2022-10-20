var updateBtns = document.getElementsByClassName("update-cart")

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var name = this.dataset.features
        var action = this.dataset.action
        console.Log('name:', name, 'action:', action)

    })
}