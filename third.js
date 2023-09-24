function solution(argv) {
    const gr = { '/': [] };
    let cur = '';
    let answer = 0;

    const child_parent = {};

    for (let i = 0; i < argv.length; i++) {
        const cmd = argv[i].split(' ');
        if (cmd[0] === 'mkdir') {
            if (cur === '') {
                gr['/'].push(cmd[1]);
                child_parent[cmd[1]] = '/';
            } else {
                const lastSlash = cur.lastIndexOf('/');
                const curFolder = cur.substring(lastSlash + 1);
                gr[curFolder].push(cmd[1]);
                child_parent[cmd[1]] = curFolder;
            }
            gr[cmd[1]] = [];
        } else if (cmd[0] === 'cd') {
            if (cmd[1] === '..') {
                const lastSlash = cur.lastIndexOf('/');
                cur = cur.slice(0, lastSlash);
            } else {
                cur += '/' + cmd[1];
            }
        } else if (cmd[0] === 'del') {
            const folderName = cmd[1];
            const lastSlash = cur.lastIndexOf('/');
            const curFolder = cur.substring(lastSlash + 1);
            gr[curFolder] = gr[curFolder].filter((f) => f !== folderName);
            delete gr[folderName];
            delete child_parent[folderName];
        } else if (cmd[0] === 'move') {
            const folderName = cmd[1];
            const src = child_parent[folderName];
            const des = cmd[2].slice(1);
            gr[src] = gr[src].filter((f) => f !== folderName);
            child_parent[folderName] = des;
            gr[des].push(folderName);
        }
    }

    const q = [];
    if (gr['/'].length === 0) {
        return 0;
    }
    for (const i of gr['/']) {
        q.push([i, 1]);
        answer = 1;
    }
    while (q.length) {
        let [cur, level] = q.shift();
        if (gr[cur].length === 0) {
            answer = Math.max(answer, level);
            continue;
        }
        for (const i of gr[cur]) {
            q.push([i, level + 1]);
        }
    }
    console.log(gr);
    console.log(child_parent);

    return answer;
}

const argv = [
    'mkdir a1',
    'mkdir a2',
    'cd a1',
    'mkdir b1',
    'cd b1',
    'mkdir c1',
    'cd c1',
    'mkdir d1',
    'cd d1',
    'mkdir e1',
    'cd ..',
    'cd ..',
    'move c1 /a2',
];
console.log(solution(argv));
