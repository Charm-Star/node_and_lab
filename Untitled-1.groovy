
import java.util.*;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); // 테스트 케이스 개수
        while(t-- > 0) {
            int i = sc.nextInt(); // 팀 개수
            int j = sc.nextInt(); // 재택 가능 업무 개수
            int k = sc.nextInt(); // 재택 불가능 업무 개수
            int l = sc.nextInt(); // 사원 수
            sc.nextLine(); // 개행문자 제거

            // 각 업무 목록 입력받기
            String[] jWork = sc.nextLine().split(" ");
            String[] kWork = sc.nextLine().split(" ");

            // 각 팀의 사원 정보 입력받기
            Map<Integer, List<Integer>> teamMap = new HashMap<>(); // 각 팀별로 사원 목록 저장
            for(int idx=0; idx<l; idx++) {
                String[] info = sc.nextLine().split(" ");
                int team = Integer.parseInt(info[0]);
                int workCount = Integer.parseInt(info[1]);
                List<String> works = Arrays.asList(sc.nextLine().split(" "));

                // 해당 사원이 재택 대상이면 팀 번호를 Map에 저장
                boolean isPossible = true;
                for(String work : works) {
                    if(!Arrays.asList(jWork).contains(work)) {
                        isPossible = false;
                        break;
                    }
                }
                if(isPossible) {
                    if(!teamMap.containsKey(team)) {
                        teamMap.put(team, new ArrayList<>());
                    }
                    teamMap.get(team).add(idx+1);
                }
            }

            // 모든 팀원이 재택 대상인 팀 중 가장 사번이 낮은 사원 출근
            boolean isAllPossible = true;
            for(Map.Entry<Integer, List<Integer>> entry : teamMap.entrySet()) {
                if(entry.getValue().size() == l/i) {
                    Collections.sort(entry.getValue());
                    System.out.print(entry.getValue().get(0) + " ");
                    isAllPossible = false;
                }
            }

            // 모든 팀에서 재택 대상이 없는 경우
            if(isAllPossible) {
                System.out.print("-1");
            }
            System.out.println();
        }
        sc.close();
    }
}
