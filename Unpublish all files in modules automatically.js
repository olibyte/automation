// ABOUT: This script checks and unpublishes all FILES on the modules page (without unpublishing files in the files page) which seem to always migrate as published in modules; William Lukamto for use in Canvas migration;

// INSTRUCTIONS: Run this script in "modules" page ONLY. When in the modules page, right-click on any part of the page, click "inspect", and click "console", paste code, press enter and let it run all the way (you may stop it at any time by refreshing the page);

var attachments = $('[data-module-type=attachment] button').toArray()

var unpublishAttachment = function(e){
    
    new Promise(function(resolve, reject){
        $(e).click()
        setTimeout(function(){
            resolve();
        }, 1000)
    })
    .then( function(){
        return new Promise(function(resolve, reject){
            $('.permissions-dialog-form .icon-unpublish').siblings('input').click() 
            $('.permissions-dialog-form button[type=submit]').click();
            setTimeout(function(){
                resolve();
            }, 1000)
        })
    }).then(function(){
        if (attachments.length > 0){
            unpublishAttachment(attachments.pop())
        }
    })
}

if (attachments.length > 0){
    unpublishAttachment(attachments.pop())
}