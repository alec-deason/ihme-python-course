def cesar_cypher_reader(message, key):
    """
    Implement a Cesar cypher decoder. In a Cesar cypher every letter in the
    regular alphabet is replaced with a letter in the cypher alphabet. For
    example if the alphabet were 'abc' and the cypher alphabet were 'cba' then
    'a' in the message would be replaced by 'c', 'b' by 'b' and 'c' by 'a'.

    The parameter `message` contains a message which has been encoded in this
    manner. `key` contains the cypher alphabet as a list of characters where
    the first character is the replacement for 'a', the second for 'b', etc.

    Use the 26 lower case english characters plus space as the alphabet.

    Return the decoded message.

    Examples
    --------
    cesar_cypher_reader('test', [' ', 'z', 'y', 'x', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']) -> 'test'
    """

    plain_text = ''
    for c in message:
        for i, cc in enumerate(key):
            if c == cc:
                plain_text = plain_text+'abcdefghijklmnopqrstuvwxyz '[i]
                break
    return ''.join(plain_text)

def cesar_cypher_writer(message, key):
    """
    Implement a Cesar cypher encoder. This should be the inverse of the
    function above. Given a `message` in plain text and the cypher alphabet
    `key` return the encoded message.
    """

    cypher_text = ''
    for c in message:
        for i, cc in enumerate('abcdefghijklmnopqrstuvwxyz '):
            if cc == c:
                cypher_text = cypher_text + key[i]
                break
    return ''.join(cypher_text)
