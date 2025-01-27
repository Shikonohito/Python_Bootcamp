function copyCode(button) {
    const codeBlock = button.nextElementSibling.querySelector('code');
    const codeText = codeBlock.textContent;

    if (navigator.clipboard) {
        navigator.clipboard.writeText(codeText)
            .then(() => changeCopyButton(button))
            .catch((err) => console.error('Не удалось скопировать текст: ', err));
    } else {
        const range = document.createRange();
        range.selectNode(codeBlock);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        document.execCommand('copy');
        selection.removeAllRanges();
        changeCopyButton(button);
    }
}

function changeCopyButton(button) {
    const originalHTML = button.innerHTML;
    button.innerHTML = `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M18.0633 5.67375C18.5196 5.98487 18.6374 6.607 18.3262 7.06331L10.8262 18.0633C10.6585 18.3093 10.3898 18.4678 10.0934 18.4956C9.79688 18.5234 9.50345 18.4176 9.29289 18.2071L4.79289 13.7071C4.40237 13.3166 4.40237 12.6834 4.79289 12.2929C5.18342 11.9023 5.81658 11.9023 6.20711 12.2929L9.85368 15.9394L16.6738 5.93664C16.9849 5.48033 17.607 5.36263 18.0633 5.67375Z" fill="currentColor"></path></svg>Copied!
    `;
    setTimeout(function () {
        button.innerHTML = originalHTML;
    }, 2000);
}