import pytest
from stacks_and_queues.stacks_and_queues import Queue #, InvalidOperationError


def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected


def test_dequeue():
    pass


def test_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


def test_peek_when_empty():
    # TODO it should raise an exception when peeking an empty queue
    pass


def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected

def test_dequeue_when_empty():
     # TODO it should raise an exception when dequeueing an empty queue
    pass


def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


def test_peek_post_dequeue():
    # TODO it should return a new first value if peek is called after a dequeue
    pass


def test_is_empty():
    #  TODO is empty should return true if no items were enqueued
    pass


def test_exhausted():
    #  TODO TODO is empty should return true after dequeueing all previously queued items
    pass
