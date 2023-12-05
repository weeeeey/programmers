import React, { useState, useEffect } from 'react';

const A = async ({ dataVersion, loadData }) => {
    try {
        await loadData().then((res) => <p>res</p>);
    } catch (error) {
        console.log('asd');
    }
};

const App = () => {
    return (
        <A
            dataVersion={10}
            loadData={() => {
                return new Promise((resolve, reject) => {
                    resolve('데이터 로드 성공');
                });
            }}
        />
    );
};

export default App;
