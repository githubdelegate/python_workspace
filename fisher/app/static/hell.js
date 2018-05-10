/*!
 *
 * ZSSRichTextEditor v0.5.2
 * http://www.zedsaid.com
 *
 * Copyright 2014 Zed Said Studio LLC
 *
 */

var zss_editor = {};

// If we are using iOS or desktop
zss_editor.isUsingiOS = true;

// If the user is draging
zss_editor.isDragging = false;

// The current selection
zss_editor.currentSelection;

// The current editing image
zss_editor.currentEditingImage;

// The current editing link
zss_editor.currentEditingLink;

// The objects that are enabled
zss_editor.enabledItems = {};

// Height of content window, will be set by viewController
zss_editor.contentHeight = 244;

// Sets to true when extra footer gap shows and requires to hide
zss_editor.updateScrollOffset = false;

/**
 * The initializer function that must be called onLoad
 */
zss_editor.init = function() {

    $('#zss_editor_content').on('touchend', function(e) {
                                zss_editor.enabledEditingItems(e);
                                var clicked = $(e.target);
                                if (!clicked.hasClass('zs_active')) {
                                $('img').removeClass('zs_active');
                                }
                                });

    $(document).on('selectionchange',function(e){
                   zss_editor.calculateEditorHeightWithCaretPosition();
                   zss_editor.setScrollPosition();
                   zss_editor.enabledEditingItems(e);
                   });

    $(window).on('scroll', function(e) {
                 zss_editor.updateOffset();
                 });

    // Make sure that when we tap anywhere in the document we focus on the editor
    $(window).on('touchmove', function(e) {
                 zss_editor.isDragging = true;
                 zss_editor.updateScrollOffset = true;
                 zss_editor.setScrollPosition();
                 zss_editor.enabledEditingItems(e);
                 });
    $(window).on('touchstart', function(e) {
                 zss_editor.isDragging = false;
                 });
    $(window).on('touchend', function(e) {
                 if (!zss_editor.isDragging && (e.target.id == "zss_editor_footer"||
                     e.target.nodeName.toLowerCase() == "html")) {
                 zss_editor.focusEditor();
                 }
                 });

}//end

zss_editor.updateOffset = function() {

    if (!zss_editor.updateScrollOffset)
        return;

    var offsetY = window.document.body.scrollTop;

    var footer = $('#zss_editor_footer');

    var maxOffsetY = footer.offset().top - zss_editor.contentHeight;

    if (maxOffsetY < 0)
        maxOffsetY = 0;

    if (offsetY > maxOffsetY)
    {
        window.scrollTo(0, maxOffsetY);
    }

    zss_editor.setScrollPosition();
}

// This will show up in the XCode console as we are able to push this into an NSLog.
zss_editor.debug = function(msg) {
    window.location = 'debug://'+msg;
}


zss_editor.setScrollPosition = function() {
    var position = window.pageYOffset;
    window.location = 'scroll://'+position;
}


zss_editor.setPlaceholder = function(placeholder) {

    var editor = $('#zss_editor_content');

    //set placeHolder
	editor.attr("placeholder",placeholder);

    //set focus
	editor.focusout(function(){
        var element = $(this);
        if (!element.text().trim().length) {
            element.empty();
        }
    });



}

zss_editor.setFooterHeight = function(footerHeight) {
    var footer = $('#zss_editor_footer');
    footer.height(footerHeight + 'px');
}

zss_editor.getCaretYPosition = function() {
    var sel = window.getSelection();
    // Next line is comented to prevent deselecting selection.
    // It looks like work but if there are any issues will appear then uconmment it as well as code above.
    //sel.collapseToStart();
    var range = sel.getRangeAt(0);
    var span = document.createElement('span');// something happening here preventing selection of elements
    range.collapse(false);
    range.insertNode(span);
    var topPosition = span.offsetTop;
    span.parentNode.removeChild(span);
    return topPosition;
}

zss_editor.calculateEditorHeightWithCaretPosition = function() {

    var padding = 50;
    var c = zss_editor.getCaretYPosition();

    var editor = $('#zss_editor_content');

    var offsetY = window.document.body.scrollTop;
    var height = zss_editor.contentHeight;

    var newPos = window.pageYOffset;

    if (c < offsetY) {
        newPos = c;
    } else if (c > (offsetY + height - padding)) {
        newPos = c - height + padding - 18;
    }

    window.scrollTo(0, newPos);
}

zss_editor.backuprange = function(){
    var selection = window.getSelection();
    var range = selection.getRangeAt(0);
    zss_editor.currentSelection = {"startContainer": range.startContainer,
        "startOffset":range.startOffset,"endContainer":range.endContainer, "endOffset":range.endOffset};
}

zss_editor.restorerange = function(){
    var selection = window.getSelection();
    selection.removeAllRanges();
    var range = document.createRange();
    range.setStart(zss_editor.currentSelection.startContainer, zss_editor.currentSelection.startOffset);
    range.setEnd(zss_editor.currentSelection.endContainer, zss_editor.currentSelection.endOffset);
    selection.addRange(range);
}

zss_editor.getSelectedNode = function() {
    var node,selection;
    if (window.getSelection) {
        selection = getSelection();
        node = selection.anchorNode;
    }
    if (!node && document.selection) {
        selection = document.selection
        var range = selection.getRangeAt ? selection.getRangeAt(0) : selection.createRange();
        node = range.commonAncestorContainer ? range.commonAncestorContainer :
        range.parentElement ? range.parentElement() : range.item(0);
    }
    if (node) {
        return (node.nodeName == "#text" ? node.parentNode : node);
    }
};


// Need way to remove formatBlock
console.log('WARNING: We need a way to remove formatBlock items');


zss_editor.insertLink = function(url, title) {

    zss_editor.restorerange();
    var sel = document.getSelection();
    console.log(sel);
    if (sel.toString().length != 0) {
        if (sel.rangeCount) {


            var el = document.createElement("a");
            el.setAttribute("href", url);
            el.setAttribute("title", title);

            var range = sel.getRangeAt(0).cloneRange();
            range.surroundContents(el);
            sel.removeAllRanges();
            sel.addRange(range);
        }
    }
    else
    {
        document.execCommand("insertHTML",false,"<a href='"+url+"'>"+title+"</a>");
    }

    zss_editor.enabledEditingItems();
}

zss_editor.updateLink = function(url, title) {

    zss_editor.restorerange();

    if (zss_editor.currentEditingLink) {
        var c = zss_editor.currentEditingLink;
        c.attr('href', url);
        c.attr('title', title);
    }
    zss_editor.enabledEditingItems();

}//end

zss_editor.updateImage = function(url, alt) {

    zss_editor.restorerange();

    if (zss_editor.currentEditingImage) {
        var c = zss_editor.currentEditingImage;
        c.attr('src', url);
        c.attr('alt', alt);
    }
    zss_editor.enabledEditingItems();

}//end

zss_editor.updateImageBase64String = function(imageBase64String, alt) {

    zss_editor.restorerange();

    if (zss_editor.currentEditingImage) {
        var c = zss_editor.currentEditingImage;
        var src = 'data:image/jpeg;base64,' + imageBase64String;
        c.attr('src', src);
        c.attr('alt', alt);
    }
    zss_editor.enabledEditingItems();

}//end


zss_editor.unlink = function() {

    if (zss_editor.currentEditingLink) {
        var c = zss_editor.currentEditingLink;
        c.contents().unwrap();
    }
    zss_editor.enabledEditingItems();
}

zss_editor.quickLink = function() {

    var sel = document.getSelection();
    var link_url = "";
    var test = new String(sel);
    var mailregexp = new RegExp("^(.+)(\@)(.+)$", "gi");
    if (test.search(mailregexp) == -1) {
        checkhttplink = new RegExp("^http\:\/\/", "gi");
        if (test.search(checkhttplink) == -1) {
            checkanchorlink = new RegExp("^\#", "gi");
            if (test.search(checkanchorlink) == -1) {
                link_url = "http://" + sel;
            } else {
                link_url = sel;
            }
        } else {
            link_url = sel;
        }
    } else {
        checkmaillink = new RegExp("^mailto\:", "gi");
        if (test.search(checkmaillink) == -1) {
            link_url = "mailto:" + sel;
        } else {
            link_url = sel;
        }
    }

    var html_code = '<a href="' + link_url + '">' + sel + '</a>';
    zss_editor.insertHTML(html_code);

}

zss_editor.prepareInsert = function() {
    zss_editor.backuprange();
}

zss_editor.insertImage = function(url, alt) {
    zss_editor.restorerange();
    var html = '<img src="'+url+'" alt="'+alt+'" />';
    zss_editor.insertHTML(html);
    zss_editor.enabledEditingItems();
}

zss_editor.insertImageBase64String = function(imageBase64String, alt) {
    zss_editor.restorerange();
    var html = '<img src="data:image/jpeg;base64,'+imageBase64String+'" alt="'+alt+'" />';
    zss_editor.insertHTML(html);
    zss_editor.enabledEditingItems();
}

zss_editor.setHTML = function(html) {
    var editor = $('#zss_editor_content');
    editor.html(html);
}

zss_editor.insertHTML = function(html) {
    document.execCommand('insertHTML', false, html);
    zss_editor.enabledEditingItems();
}

zss_editor.getHTML = function() {

    // Images
    var img = $('img');
    if (img.length != 0) {
        $('img').removeClass('zs_active');
        $('img').each(function(index, e) {
                      var image = $(this);
                      var zs_class = image.attr('class');
                      if (typeof(zs_class) != "undefined") {
                      if (zs_class == '') {
                      image.removeAttr('class');
                      }
                      }
                      });
    }

    // Blockquote
    var bq = $('blockquote');
    if (bq.length != 0) {
        bq.each(function() {
                var b = $(this);
                if (b.css('border').indexOf('none') != -1) {
                b.css({'border': ''});
                }
                if (b.css('padding').indexOf('0px') != -1) {
                b.css({'padding': ''});
                }
                });
    }

    // Get the contents
    var h = document.getElementById("zss_editor_content").innerHTML;

    return h;
}

zss_editor.getText = function() {
    return $('#zss_editor_content').text();
}

zss_editor.isCommandEnabled = function(commandName) {
    return document.queryCommandState(commandName);
}


zss_editor.focusEditor = function() {

    // the following was taken from http://stackoverflow.com/questions/1125292/
    // how-to-move-cursor-to-end-of-contenteditable-entity/3866442#3866442
    // and ensures we move the cursor to the end of the editor
    var editor = $('#zss_editor_content');
    var range = document.createRange();
    range.selectNodeContents(editor.get(0));
    range.collapse(false);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    editor.focus();
}

zss_editor.blurEditor = function() {
    $('#zss_editor_content').blur();
}

zss_editor.setCustomCSS = function(customCSS) {

    document.getElementsByTagName('style')[0].innerHTML=customCSS;

    //set focus
    /*editor.focusout(function(){
                    var element = $(this);
                    if (!element.text().trim().length) {
                    element.empty();
                    }
                    });*/



}

//end
