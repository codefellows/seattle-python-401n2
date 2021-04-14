import Link from 'next/link'

export default function CookieStandHeader({ username, onLogout }) {
    return (
        <header >
            <h1 >
                Cookie Stand Admin
                </h1>
            <div >
                <p >{username}</p>
                <Link href="/">
                    <a onClick={onLogout} >Sign Out</a>
                </Link>
                <nav>
                    <Link href="/overview"><a>Overview</a></Link>
                </nav>
            </div>
        </header>
    )
}
