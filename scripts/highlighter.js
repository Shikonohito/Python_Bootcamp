document.addEventListener('DOMContentLoaded', function () {
    const codeBlocks = document.querySelectorAll('code.python');
    codeBlocks.forEach(function (codeBlock, index) {
        let innerHTML = codeBlock.innerHTML;
        console.log(index, innerHTML);
        // STRING
        let regex = /(?<!\\)(f?"[^"\\]*(?:\\.[^"\\]*)*")/g;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="string">${match}</span>`;
        });
        regex = /(?<!\\)(f?'[^'\\]*(?:\\.[^'\\]*)*')/g;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="string">${match}</span>`;
        });
        // KEYWORD CLASS
        regex = /(class)(?!=)/g;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="keyword">${match}</span>`;
        });
        // KEYWORDS
        const keywords = [
            'def', 'for', 'in', 'while', 'and', 'or', 'not',
            'if', 'elif', 'else', 'continue', 'break', 'try', 'with',
            'as', 'except', 'finally', 'return', 'True', 'False', 'from', 'import', 'del', 'None',
            'pass'
        ];
        regex = new RegExp(`\\b(${keywords.join('|')})\\b`, 'g');
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="keyword">${match}</span>`;
        });
        // KEYWORD NUMBER
        regex = /\b\d+(\.\d+)?/g;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="number">${match}</span>`;
        });
        // STRING-ESC
        regex = /\\./g;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="string-esc">${match}</span>`;
        });
        // COMMENTS
        regex = /(#.*$)/gm;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="comments">${match}</span>`;
        });
        // METADATA
        regex = /^(\s*@\w+)/gm;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="metadata">${match}</span>`;
        });
        // SELF
        regex = /\bself\b/g;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="self">${match}</span>`;
        });
        // BUILT-IN
        regex = /\b(open|print|input|int|float|str|list|set|dict|range|len|sum|min|max|sort|bool)\b/g;
        innerHTML = innerHTML.replace(regex, (match) => {
            return `<span class="built-in">${match}</span>`;
        });
        // FUNCTION
        regex = /(<span class="keyword">def<\/span>)\s(\w+)\(/g;
        innerHTML = innerHTML.replace(regex, '$1 <span class="function">$2</span>(');
        // SPECIAL-NAMES
        regex = /(<span class="function">)(__\w+__)(<\/span>)/g;
        innerHTML = innerHTML.replace(regex, '$1<span class="special-names">$2</span>$3');
        // KEYWORD-ARGUMENT
        regex = /, (end|sep)=/g;
        innerHTML = innerHTML.replace(regex, ', <span class="keyword-argument">$1</span>=');
        codeBlock.innerHTML = innerHTML
    });
});