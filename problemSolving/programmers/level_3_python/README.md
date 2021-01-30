# Level 3 (Python)

## 목차

* [베스트앨범](#베스트앨범)
* [배달](#배달)

## 베스트앨범

* [문제링크](https://programmers.co.kr/learn/courses/30/lessons/42579)

* 풀이

  ```python
  def solution(genres, plays):
      answer = []
      music = {}
      for i in range(len(genres)):
          if genres[i] not in music:
              music[genres[i]] = {"total": plays[i], "idx": [i]}
          else:
              music[genres[i]]["total"] += plays[i]
              music[genres[i]]["idx"].append(i)
      sortedGenres = sorted(set(genres), key=lambda x: music[x]["total"], reverse=True)
      for i in range(len(sortedGenres)):
          answer += sorted(music[sortedGenres[i]]["idx"], key=lambda x: (plays[x], -x), reverse=True)[:2]
      return answer
  ```

  * 해시를 통해 정렬에서 기준이 될 Total plays값과 장르에 속한 고유번호들을 찾아주고

    이를 기준으로 정렬하여 문제를 해결하였다.

## 배달

* [문제링크](https://programmers.co.kr/learn/courses/30/lessons/12978)

* 풀이

  ```python
  def solution(N, road, K):
      answer = 0
      graph = [[] for _ in range(N + 1)]
      width = [0xffffff]*(N+1)
      width[1] = 0
      for li in road:
          graph[li[0]].append((li[1], li[2]))
          graph[li[1]].append((li[0], li[2]))
      
      
      def DFS(now, count):
          for nxt in graph[now]:
              if width[nxt[0]] > count + nxt[1]:
                  width[nxt[0]] = count + nxt[1]
                  DFS(nxt[0], width[nxt[0]])
                  
      DFS(1, 0)
      for num in width:
          if num <= K:
              answer += 1
      return answer
  ```

  * 2차원 리스트로 그래프를 만들어주고 DFS를 통해 가중치가 가장 적을때의 값을 저장해주었다.

    많이 쓰이는 알고리즘이었는데 이름이 기억이 안난다... 나중에 찾게되면 추가해야지!