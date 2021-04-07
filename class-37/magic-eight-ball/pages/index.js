import Head from 'next/head'
import { useState } from 'react'

export default function Home() {

  const [question, setQuestion] = useState('Your Question Will Go Here!')
  const [reply, setReply] = useState("Ask Me Anything!")

  function questionAskedHandler(event){
    event.preventDefault();
    // alert(event.target.question.value)
    const randomReply = Math.random() > .5 ? "Yes" : "No";

    setReply(randomReply)
    setQuestion(event.target.question.value)
  }

  return (
    <div className="">
      <Head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Header title="Magic 8 Ball"/>
      {/* <header className="flex p-4 bg-gray-500 text-gray-50">
        <h1 className="text-4xl border border-color-black">Magic 8 Ball</h1>
      </header> */}

      <main className="">
        <form onSubmit={questionAskedHandler} className="flex w-1/2 p-2 mx-auto my-4 bg-gray-500">
          <input name="question" className="flex-auto pl-1"></input>
          <button className="px-2 py-1 by-gray-500 text-gray-50">Ask</button>
        </form>

      <div className="mx-auto bg-gray-900 rounded-full w-96 h-96">
        <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
          <p>{reply}</p>
        </div>
      </div>

      <h3 className="p-1 text-2xl text-center border">{question}</h3>

      </main>

      <footer className="p-4 mt-8 bg-gray-500 ">
        <p className="text-center text-gray-50">Code Fellows</p>
      </footer>
    </div>
  )

  function Header(props){
    return(
      <header className="flex p-4 bg-gray-500 text-gray-50">
        <h1 className="text-4xl border border-color-black">{props.title}</h1>
      </header>
    )
  }
}
