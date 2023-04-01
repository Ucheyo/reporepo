var today = new Date();
var todayDate = today.getDate();
var threads = [
    {
        id: 1,
        title: "Thread 1",
        authour: "Aaron",
        //date: todayDate,
        date: Date.now(),
        content: "Thread content",
        comments: [
            {
                authour: "Jack",
                date: Date.now(),
                content: "Hey there",
            },
            {
                authour: "Arthur",
                date: Date.now(),
                content: "Hey you too",
            }
        ]
    },

    {
        id: 2,
        title: "Thread 2",
        authour: "John",
        date: Date.now(),
        //date: todayDate,
        content: "Thread content",
        comments: [
            {
                authour: "Philip",
                date: Date.now(),
                content: "Hey there",
            },
            {
                authour: "Andrew",
                date: Date.now(),
                content: "Hey you too",
            }
        ]
    }
]