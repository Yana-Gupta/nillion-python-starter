from nada_dsl import *

def nada_main():
    # Define parties
    alice = Party(name="Alice")
    bob = Party(name="Bob")

    # Define secret votes from each party
    alice_vote = SecretInteger(Input(name="alice_votes", party=alice))
    bob_vote = SecretInteger(Input(name="bob_votes", party=bob))

    alice_has_max_vote = (alice_vote > bob_vote) 
    bob_has_max_vote = (bob_vote > alice_vote) 

    alice_wins = alice_has_max_vote
    bob_wins = bob_has_max_vote

    alice_output = Output(alice_wins, "alice_wins", alice)
    bob_output = Output(bob_wins, "bob_wins", bob)

    return [alice_output, bob_output]

