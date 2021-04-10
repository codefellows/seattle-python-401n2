import Head from 'next/head'
import Link from 'next/link'

import { replies } from '../data'
import { useState} from 'react'

export default function Home() {

  // const [reply, setReply] = useState('Ask ME Anything!')
  const [answeredQuestions, setAnsweredQuestions] = useState([]);

  function questionAskedHandler(event){
    event.preventDefault();

    const randomReply = replies[Math.floor(Math.random() * replies.length)]

    const answeredQuestion = {
      question: event.target.question.value,
      reply: randomReply,
      id: answeredQuestions.length,
    }

    setAnsweredQuestions([...answeredQuestions, answeredQuestion])
  // console.log('answeredQuestion', answeredQuestion)

    // setReply(randomReply);
  }

  function getLatestReply(){
    if(answeredQuestions.length === 0){
      return 'Ask Me Anythin!'
    }
    return answeredQuestions[answeredQuestions.length -1].reply
  }
    

  return (
    <div className="">
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="">
        <Header title="Magic 8 Ball" answeredQuestionsArray = {answeredQuestions}/>
        <QuestionForm />
        <EightBall latestReply={getLatestReply()}/>
        <ResponceTable answeredQuestionsArray = {answeredQuestions} />
        <Footer />
      </main>

    </div>
  )

  function Header(props){
    return(
      <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
        <h1 className="text-4xl">{props.title}</h1>
        <p>{props.answeredQuestionsArray.length} questions answered</p>
      </header>
    )
  }

  function QuestionForm(props){
    return(
      <form onSubmit={questionAskedHandler} className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
        <input name="question" className="flex-auto pl-1" />
        <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
      </form>
    )
  }

  function EightBall(props){
    return(
      <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
        <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
          <p className="text-xl text-center">{props.latestReply}</p>
        </div>
      </div>
    )
  }

  function ResponceTable(props){
    console.log(props.answeredQuestionsArray)
    return(
      <table className="w-1/2 mx-auto my-4">
        <thead>
          <tr>
            <th className="border border-gray-700">No.</th>
            <th className="border border-gray-700">Question</th>
            <th className="border border-gray-700">Responce</th>
          </tr>
        </thead>
        <tbody>
          {props.answeredQuestionsArray.map(item =>(
            <tr className="odd:bg-red-500">
              <td className="pl-2 border border-gray-700">{item.id}</td>
              <td className="pl-2 border border-gray-700">{item.question}</td>
              <td className="pl-2 border border-gray-700">{item.reply}</td>
            </tr>
          ))}

        </tbody>
        
      </table>
    )
  }

  function Footer(props){
    return(
      <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
        <nav>
          {/* <a href="careers">Careers</a> */}
          <Link href="/careers">
            <a>Careers</a>
          </Link>
        </nav>
      </footer>
    )
  }

}
